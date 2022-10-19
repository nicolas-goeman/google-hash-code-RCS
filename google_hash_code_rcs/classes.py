from xmlrpc.client import Boolean

# ================================== #
#       ARCHITECTURE CLASSES         #
# ================================== #

class Binary:
    def __init__(self, id) -> None:
        self.services = []
        self.engineers = []
        self.id = id
    
    def add_engineer(self, engineer) -> None:  # pragma: no cover
        self.engineers.append(engineer)
    
    def remove_engineer(self, engineer) -> None:  # pragma: no cover
        self.engineers.remove(engineer)
    
    def add_service(self, service) -> None:  # pragma: no cover
        self.services.append(service)
    
    def remove_service(self, service) -> None:  # pragma: no cover
        self.services.remove(service)
    
    def get_n_services(self) -> int:  # pragma: no cover
        return len(self.services)

    def get_n_engineers(self) -> int:  # pragma: no cover
        return len(self.engineers)   


class Service:
    def __init__(self, name, binary: Binary) -> None:
        self.name = name
        self.binary = binary
        self.binary.add_service(self)
        self.features = []
    
    def add_feature(self, feature) -> None:  # pragma: no cover
        self.features.append(feature)


class Feature:
    def __init__(self, services: list[Service], users: int, difficulty: int, name: str) -> None:
        self.name = name
        self.services = []
        for service in services:
            self.add_service(service)

        self.users = users
        self.difficulty = difficulty
    
    def add_service(self, service: Service) -> None:  # pragma: no cover
        self.services.append(service)
        service.add_feature(self)
    
    def is_launched(self) -> Boolean:
        return len(self.services) == 0
    
    def remove_service(self, service) -> None:  # pragma: no cover
        self.services.remove(service)

# ================================== #
#           ENGINEER CLASS           #
# ================================== #

class Engineer:
    def __init__(self, id) -> None:
        self.id = id
        self.tasks = []
        self.current_task = None
        self.is_available = True
    
# ================================== #
#           TASKS CLASSES            #
# ================================== #

class Task:
    def __init__(self, type):
        self.type = type

class ImplementFeature(Task):
    def __init__(self, feature: Feature, binary: Binary, engineer: Engineer) -> None:
        super().__init__(type="ImpFeat")
        self.feature = feature
        self.binary = binary
        self.engineer = engineer

        self.engineer.is_available = False

        self.total_days = self.compute_difficulty()
        self.remaining_days = self.total_days
        
        self.binary.engineers.append(engineer)

        self.engineer.tasks.append(self)
        self.engineer.current_task = self
    
    def compute_difficulty(self) -> int:
        return self.feature.difficulty + len(self.binary.services) + len(self.binary.engineers)

class Wait(Task):    
    def __init__(self, days: int, engineer: Engineer) -> None:
        super().__init__(type="Wait")
        self.engineer = engineer
        
        self.engineer.is_available = False

        self.total_days = days
        self.remaining_days = self.total_days

        self.engineer.tasks.append(self)
        self.engineer.current_task = self
