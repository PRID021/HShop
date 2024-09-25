class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {"auth", "contenttypes"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth' database.
        """
        if app_label in self.route_app_labels:
            return db == "auth"
        return None


class PollsRouter:
    """
    A router to control all database operations on models in the
    polls applications.
    """

    route_app_labels = {"polls"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read polls and contenttypes models go to polls.
        """
        if model._meta.app_label in self.route_app_labels:
            return "polls"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write polls and contenttypes models go to polls.
        """
        if model._meta.app_label in self.route_app_labels:
            return "polls"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the polls or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the polls and contenttypes apps only appear in the
        'polls' database.
        """
        if app_label in self.route_app_labels:
            return db == "polls" and app_label == "polls"
        return False


class AskServiceRouter:
    """
    A router to control all database operations on models in the
    askservice applications.
    """

    route_app_labels = {"askservice"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read askservice and contenttypes models go to askservice.
        """
        if model._meta.app_label in self.route_app_labels:
            return "askservice"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write askservice and contenttypes models go to askservice.
        """
        if model._meta.app_label in self.route_app_labels:
            return "askservice"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the askservice or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the askservice and contenttypes apps only appear in the
        'askservice' database.
        """
        if app_label in self.route_app_labels:
            return db == "askservice" and app_label == "polls"
        return None
