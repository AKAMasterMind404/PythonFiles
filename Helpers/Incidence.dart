class Incidence {
  final String type; 
  final String area; 
  final String location; 
  final String actionTaken; 
  final DateTime occurredAt; 
  final DateTime notedAt; 
  final List photos; 

  const Incidence({
      required this.type, 
      required this.area, 
      required this.location, 
      required this.actionTaken, 
      required this.occurredAt, 
      required this.notedAt, 
      required this.photos, 
  });

  Incidence copy({
          String? type, 
          String? area, 
          String? location, 
          String? actionTaken, 
          DateTime? occurredAt, 
          DateTime? notedAt, 
          List? photos, 
          }) => 
      Incidence(
        type: type ?? this.type, 
        area: area ?? this.area, 
        location: location ?? this.location, 
        actionTaken: actionTaken ?? this.actionTaken, 
        occurredAt: occurredAt ?? this.occurredAt, 
        notedAt: notedAt ?? this.notedAt, 
        photos: photos ?? this.photos, 
      ); 

  static Incidence fromJson(Map<String, Object?> json) => Incidence(
        type: json[IncidenceFields.type] as String,
        area: json[IncidenceFields.area] as String,
        location: json[IncidenceFields.location] as String,
        actionTaken: json[IncidenceFields.actionTaken] as String,
        occurredAt: json[IncidenceFields.occurredAt] as DateTime,
        notedAt: json[IncidenceFields.notedAt] as DateTime,
        photos: json[IncidenceFields.photos] as List,
      );

  Map<String, Object?> toJson() => {
        IncidenceFields.type: type,
        IncidenceFields.area: area,
        IncidenceFields.location: location,
        IncidenceFields.actionTaken: actionTaken,
        IncidenceFields.occurredAt: occurredAt.toIso8601String(),
        IncidenceFields.notedAt: notedAt.toIso8601String(),
        IncidenceFields.photos: photos,
      };
}
