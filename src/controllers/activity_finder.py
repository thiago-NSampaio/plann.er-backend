from collections import defaultdict


class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def finder(self, trip_id: str) -> dict:
        try:
            # Obtenha atividades para a viagem especificada
            activities = self.__activities_repository.find_activities_from_trip(
                trip_id)
            grouped_activities = defaultdict(list)

            # Agrupe atividades por data
            for activity in activities:
                # Acesse atributos diretamente dos objetos Activity
                date = activity.occurs_at.strftime(
                    '%Y-%m-%d')  # Formata a data
                grouped_activities[date].append({
                    "id": activity.id,
                    "trip_id": activity.trip_id,
                    "title": activity.title,
                    "occurs_at": activity.occurs_at.isoformat()  # Formata a data e hora
                })

            # Formate a lista de atividades agrupadas
            formatted_activity = [
                {"date": date, "activities": acts}
                for date, acts in grouped_activities.items()
            ]

            return {
                "body": {"activities": formatted_activity},
                "status_code": 200
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400
            }
