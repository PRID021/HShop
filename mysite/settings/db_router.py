class AppRouter:
    """A router to control all database operations for different apps."""

    def db_for_read(self, model, **hints):
        """Point all read operations to the appropriate database."""
        if model._meta.app_label == "polls":
            return "polls_db"

        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the appropriate database."""
        if model._meta.app_label == "polls":
            return "polls_db"

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the app is involved."""
        if obj1._meta.app_label == "polls" or obj2._meta.app_label == "polls":
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the apps only appear in the specified databases."""
        if app_label == "polls":
            return db == "polls_db"
        return None
