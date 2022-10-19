

class Binary:
    def __init__(self) -> None:
        self.services = []
        self.engineers = []
    
    def add_engineer(self, engineer) -> None:
        self.engineers.append(engineer)
    
    def remove_engineer(self, engineer) -> None:
        self.engineers.remove(engineer)
    
    def get_n_services(self) -> int:
        return len(self.services)

    def get_n_engineers(self) -> int:
        return len(self.engineers)
    

class Service:
    def __init__(self, binary) -> None:
        self.binary = binary
        self.features = []
    
    def add_feature(self, feature) -> None:
        self.features.append(feature)


class Feature:
    def __init__(self, services: list[Service], users: int, difficulty: int) -> None:
        self.services = []
        for service in self.services:
            self.add_service(service)

        self.users = users
        self.difficulty = difficulty
    
    def add_service(self, service: Service) -> None:
        self.services.append(service)
        service.add_feature(self)

class Engineer:
    def __init__(self, id) -> None:
        self.id = id
        self.tasks = []
        self.current_task = None
        self.is_available = True
    