import os

BOOLEAN = "bool"
INTEGER = "int"
FLOAT = "float"
STRING = "str"
LIST = "list"
DICT = "dict"


class GenerateScripts:
    def __init__(self, name: str, params: list):
        self.name = name
        self.params = params

    def _copyContentsInAList(self, path: str):
        lines = []
        with open(path, encoding="utf8", errors="surrogateescape") as f:
            [lines.append(i) for i in f if len(i.strip())]
        return lines

    def _getDataType(self, data_type: str, isInterface: bool):
        _map = {
            BOOLEAN: "boolean" if isInterface else "Boolean",
            FLOAT: "number" if isInterface else "Number",
            INTEGER: "number" if isInterface else "Number",
            STRING: "string" if isInterface else "String",
            LIST: "Array<any>" if isInterface else "Array",
            DICT: "any" if isInterface else "Map",
        }

        return _map[data_type]

    def _getDirectoryPath(self, place: str):
        s = "\src"
        _map = {
            "home": "",
            "models": f"{s}\\models",
            "interfaces": f"{s}\\interfaces",
            "services": f"{s}\\services",
            "utils": f"{s}\\utils",
            "routes": f"{s}\\api\\routes",
            "middlewares": f"{s}\\api\\middlewares",
            "config": f"{s}\\config",
            "loaders": f"{s}\\loaders",
            "types": f"{s}\\types\\express",
            "loader-index": f"{s}\\loaders\\index.ts",
            "express-index": f"{s}\\types\\express\\index.d.ts",
            "route-index": f"{s}\\api\\index.ts",
        }
        suffix = _map.get(place)
        assert bool(suffix), "Please request for a valid directory"

        return os.path.join(os.path.dirname(__file__) + suffix)

    def createInterface(self):
        path = self._getDirectoryPath("interfaces")
        interface_file = f"I{self.name}.ts"

        with open(os.path.join(path, interface_file), 'w') as f:
            f.write(f"export interface I{self.name} " + '{\n')
            f.write("  _id: string;\n")

            for param, _type in self.params:
                prop_type = self._getDataType(_type, isInterface=True)
                f.write(f"  {param}:{prop_type};\n")

            f.write('}\n')

    def createModel(self):
        path = self._getDirectoryPath("models")
        file = f"{self.name.lower()}.ts"

        with open(os.path.join(path, file), 'w') as f:
            f.write("import { " + f"I{self.name}" + " } " + f" from '../interfaces/I{self.name}';\n")
            f.write(f"import mongoose from 'mongoose';\n\n")

            f.write(f"const model = new mongoose.Schema(\n")
            f.write("{\n")
            for param, _type in self.params:
                prop_type = self._getDataType(_type, isInterface=False)
                f.write(f"    {param}: " + "{\n")
                f.write(f"      type: {prop_type},\n")
                f.write("    },\n")
            f.write("},\n{ timestamps: true });\n\n")
            f.write(
                f"export default mongoose.model<I{self.name} & mongoose.Document>('{self.name.lower()}Model', model);\n")

    def registerModel(self):
        loaders_index = self._getDirectoryPath("loader-index")
        loaders_lines = self._copyContentsInAList(loaders_index)

        # REGISTERING MODEL INSIDE loaders/index.ts
        with open(loaders_index, "w+", encoding="utf8", errors="surrogateescape") as _:
            model_line = f"  const {self.name.lower()}Model = " + " {\n" + \
                         f"      name: '{self.name.lower()}Model',\n" + \
                         f"      model: require('../models/{self.name.lower()}').default,\n" + \
                         "};\n"
            for line in loaders_lines:
                if line.strip() == "Logger.info('✌️ DB loaded and connected!');":
                    _.write(line + "\n")
                    _.write(model_line)
                elif line.strip() == "models: [":
                    _.write(line)
                    _.write(f"      {self.name.lower()}Model,\n")
                else:
                    _.write(line)

        # REGISTERING MODEL INSIDE loaders/types/express/index.ts
        loaders_express = self._getDirectoryPath("express-index")
        loaders_lines = self._copyContentsInAList(loaders_express)

        with open(loaders_express, "w+", encoding="utf8", errors="surrogateescape") as _:
            import_line = f"import " + "{ " + f"I{self.name}" + "}" + f" from '../../interfaces/I{self.name}';\n"
            export_line = f"    export type {self.name.lower()}Model = Model<I{self.name} & Document>\n"

            for line in loaders_lines:
                if line.strip() == "import { type } from 'os';":
                    _.write(line)
                    _.write(import_line)
                elif line.strip() == "namespace Models {":
                    _.write("\n" + line)
                    _.write(export_line)
                else:
                    _.write(line)

    def createService(self):
        path = self._getDirectoryPath("services")
        service_file = f"{self.name.lower()}.ts"

        with open(os.path.join(path, service_file), 'w') as f:
            f.write("import { Service, Inject, Container } from 'typedi';\n")
            f.write("import { " + f"I{self.name}" + " } " + f"from '../interfaces/I{self.name}';\n")
            f.write("import HelperService from '../utils/helpers';\n\n")
            f.write(f"@Service()\n")
            f.write(f"export default class {self.name}Service " + "{\n")
            f.write(f"  private helperService: HelperService;\n\n")
            f.write(f"  constructor(\n")
            f.write(f"    @Inject('{self.name.lower()}Model') "
                    f"private {self.name.lower()}Model: "
                    f"Models.{self.name.lower()}Model) " + "{\n")
            f.write(f"    this.helperService = Container.get(HelperService);\n")
            f.write("  }\n\n")
            f.write(f"  public async f(): Promise<any> " + "{\n")
            f.write("  }\n")
            f.write("}\n\n")

    def createRoute(self):
        path = self._getDirectoryPath("routes")
        route_file = f"{self.name.lower()}.ts"

        with open(os.path.join(path, route_file), 'w') as f:
            f.write("import { Router, Request, Response, NextFunction } from 'express';\n")
            f.write("import { Container } from 'typedi';\n")
            f.write(f"import {self.name}Service from '../../services/{self.name.lower()}';\n")
            f.write("import middlewares from '../middlewares';\n\n")
            f.write("const route = Router();\n\n")
            f.write("export default (app: Router) => {\n")
            f.write(f"  app.use('/{self.name.lower()}', route);\n")
            f.write(f"  const {self.name.lower()}Service = Container.get({self.name}Service)\n\n")

            for req in ["post", "get", "put", "delete"]:
                f.write(f"  route.{req}('/', "
                        f"middlewares.attachCurrentUser, "
                        f"async (req: Request, res: Response) => " + "{\n")
                f.write("    try{\n\n")
                f.write("    }\n")
                f.write("    catch (e) {\n")
                f.write("      return res.status(500).json({ 'error': `${e.message.toString()}` });")
                f.write("    }\n")
                f.write("  });\n\n")
            f.write("}")

    def registerRoute(self):
        index_file = self._getDirectoryPath("route-index")
        loaders_lines = self._copyContentsInAList(index_file)
        import_line = f"import {self.name.lower()} from './routes/{self.name.lower()}';\n"

        with open(index_file, "w", encoding="utf8", errors="surrogateescape") as _:
            for line in loaders_lines:
                if line.strip() == "import { Router } from 'express';":
                    _.write(line)
                    _.write(import_line)
                elif line.strip() == "const app = Router();":
                    _.write(line)
                    _.write(f"	{self.name.lower()}(app);\n")
                else:
                    _.write(line)

    def runAllScripts(self):
        self.createInterface()
        self.createModel()
        self.registerModel()
        self.createService()
        self.createRoute()
        self.registerRoute()


o1: GenerateScripts = GenerateScripts(
    "Note",
    [
        ("name", STRING),
        ("age", INTEGER),
        ("isAdult", BOOLEAN),
        ("score", FLOAT),
        ("listIds", LIST),
        ("some1", DICT),
    ],
)

o1.runAllScripts()
