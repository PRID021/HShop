class AppRouter:
    """
    A router to control database operations for authentication (auth app) and two apps (app1 and app2).
    Routes:
    - Auth and related tables to 'auth_db'
    - App1 models to 'app1_db'
    - App2 models to 'app2_db'
    """

    def db_for_read(self, model, **hints):
        """
        Direct read operations to the appropriate database.
        - User/authentication models go to 'auth_db'
        - App1 models go to 'app1_db'
        - App2 models go to 'app2_db'
        """
        if (
            model._meta.app_label == "auth"
            or model._meta.app_label == "contenttypes"
            or model._meta.app_label == "sessions"
        ):
            return "auth_db"
        if model._meta.app_label == "polls":
            return "polls_db"
        if model._meta.app_label == "askservice":
            return "askservice_db"

        return None

    def db_for_write(self, model, **hints):
        """
        Direct write operations to the appropriate database.
        - User/authentication models go to 'auth_db'
        - App1 models go to 'app1_db'
        - App2 models go to 'app2_db'
        """
        if (
            model._meta.app_label == "auth"
            or model._meta.app_label == "contenttypes"
            or model._meta.app_label == "sessions"
        ):
            return "auth_db"
        if model._meta.app_label == "polls":
            return "polls_db"
        if model._meta.app_label == "askservice":
            return "askservice_db"

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations between models in the same database.
        For instance, users and permissions (from auth app) should relate to each other.
        """
        if (
            obj1._meta.app_label == "auth"
            or obj1._meta.app_label == "contenttypes"
            or obj1._meta.app_label == "sessions"
        ) and (
            obj2._meta.app_label == "auth"
            or obj2._meta.app_label == "contenttypes"
            or obj2._meta.app_label == "sessions"
        ):
            return True
        if obj1._meta.app_label == "polls" or obj2._meta.app_label == "polls":
            return True
        if obj1._meta.app_label == "askservice" or obj2._meta.app_label == "askservice":
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure the auth app only appears in 'auth_db', and the respective apps only appear in their databases.
        """
        if (
            app_label == "auth"
            or app_label == "contenttypes"
            or app_label == "sessions"
        ):
            return db == "auth_db"
        if app_label == "polls":
            return db == "polls_db"
        if app_label == "askservice":
            return db == "askservice_db"
        return None
