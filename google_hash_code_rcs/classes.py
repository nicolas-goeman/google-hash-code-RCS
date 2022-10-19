from xmlrpc.client import Boolean

# ================================== #
#       ARCHITECTURE CLASSES         #
# ================================== #

class Binary:
    def __init__(self, id) -> None:
        """It define a list of services, engineers and an id.
        Args:
        self represents the instance of the class
        id
        """
        self.services = []
        self.engineers = []
        self.id = id
    
    def add_engineer(self, engineer) -> None:  # pragma: no cover
        """It  adds to engineers list a new engineer working on binary
        Args:
        self represents the instance of the class
        engineer (Int): engineer ready to work

        Return: updated list with new engineers
        """
        self.engineers.append(engineer)
    
    def remove_engineer(self, engineer) -> None:  # pragma: no cover
        """It removes to engineers list a engineer working on binary
        Args:
        self represents the instance of the class
        engineer (Int): engineer to remove

        Return: updated list of engineers
        """

        self.engineers.remove(engineer)
    
    def add_service(self, service) -> None:  # pragma: no cover
        """It adds to services list a service part of a binary
        Args:
        self represents the instance of the class
        service (Int): service to add

        Return: updated list of services
        """
        self.services.append(service)
    
    def remove_service(self, service) -> None:  # pragma: no cover
        """It removes to services list a service part of a binary
        Args:
        self represents the instance of the class
        service (Int): service to remove

        Return: updated list of services
        """
        self.services.remove(service)
    
    def get_n_services(self) -> int:  # pragma: no cover
        """It returns the number of services
        Args:
        self represents the instance of the class

        Return: (Int) number of services
        """
        return len(self.services)

    def get_n_engineers(self) -> int:  # pragma: no cover
        """It returns the number of engineers
        Args:
        self represents the instance of the class

        Return: (Int) number of engineers
        """
        return len(self.engineers)   


class Service:
    def __init__(self, name, binary: Binary) -> None:
        """It define a list of features.
        Args:
        self represents the instance of the class
        name: name of service
        binary: binary where service is 
        """
        self.name = name
        self.binary = binary
        self.binary.add_service(self)
        self.features = []
    
    def add_feature(self, feature) -> None:  # pragma: no cover
        """It adds to features list a feature relied on a service
        Args:
        self represents the instance of the class
        feature (Int): feature to add

        Return: updated list of features
        """
        self.features.append(feature)


class Feature:
    def __init__(self, services: list[Service], users: int, difficulty: int, name: str) -> None:
        """It define a list of services, the number of daily users that benefit from the feature and his difficulty.
        Args:
        self represents the instance of the class
        services: list of Service Class
        users: users that benefit from the feature
        difficulty: the difficulty of feature
        """
        self.name = name
        self.services = []
        for service in services:
            self.add_service(service)

        self.users = users
        self.difficulty = difficulty
    
    def add_service(self, service: Service) -> None:  # pragma: no cover
        """It adds the features to the respective services where they are running
        Args:
        self represents the instance of the class
        service: service class

        Return: updated list of services
        """
        self.services.append(service)
        service.add_feature(self)
    
    def is_launched(self) -> Boolean:
        """It returns the features that are already launched 
        Args:
        self represents the instance of the class

        Return (Boolean): features already launched
        """
        return len(self.services) == 0
    
    def remove_service(self, service) -> None:  # pragma: no cover
        self.services.remove(service)

# ================================== #
#           ENGINEER CLASS           #
# ================================== #

class Engineer:
    def __init__(self, id) -> None:
        """It define a list of tasks, the id, the current task and the availability of an engineer.
        Args:
        self represents the instance of the class
        id
        """
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
        """It recalls the feature, binary, engineer classes.

        Args:
        self represents the instance of the class
        feature: Feature class
        binary: Binary class
        engineer: Engineer class

        """
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
        """It  returns the result obtained by the calculation of difficulty to implement a feature
        Args:
        self represents the instance of the class
        Return (Int) value of difficulty

        """
        return self.feature.difficulty + len(self.binary.services) + len(self.binary.engineers)

class Wait(Task):    
    def __init__(self, days: int, engineer: Engineer) -> None:
        """It updates the remaining working days and the total days.
        Args:
        self represents the instance of the class
        days (Int): total days of work
        engineer: Engineer class

        """
        super().__init__(type="Wait")
        self.engineer = engineer
        
        self.engineer.is_available = False

        self.total_days = days
        self.remaining_days = self.total_days

        self.engineer.tasks.append(self)
        self.engineer.current_task = self
