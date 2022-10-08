import expressLoader from './express';
import dependencyInjectorLoader from './dependencyInjector';
import mongooseLoader from './mongoose';
import jobsLoader from './jobs';
import Logger from './logger';

export default async ({ expressApp }) => {
    const mongoConnection = await mongooseLoader();
Logger.info('✌️ DB loaded and connected!');

const testModel = {
    name: 'testModel',
    model: require('../models/test').default,
};

const roomModel = {
    name: 'roomModel',
    model: require('../models/room').default,
};

const userModel = {
    name: 'userModel',
    model: require('../models/user').default,
};

const { logger } = await dependencyInjectorLoader({
    mongoConnection,
    models: [
                testModel,
                userModel,
                roomModel
            ],
});
Logger.info('✌️ Dependency Injector loaded');


await expressLoader({ app: expressApp });
Logger.info('✌️ Express loaded');
};
