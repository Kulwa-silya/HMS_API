from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit an object.
    Read-only access is allowed for any authenticated user.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff

class IsDoctor(permissions.BasePermission):
    """
    Custom permission to only allow users in the 'Doctor' group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Doctor').exists()

class IsNurse(permissions.BasePermission):
    """
    Custom permission to only allow users in the 'Nurse' group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Nurse').exists()

# Example of a more complex permission for object-level checks
# class IsOwnerOrAdmin(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object or admins to edit it.
#     Assumes the instance has an 'owner' or 'user' attribute.
#     """
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Write permissions are only allowed to the owner of the snippet or an admin.
#         # This assumes your model instance has an `owner` or `user` attribute.
#         owner_field = None
#         if hasattr(obj, 'owner'):
#             owner_field = obj.owner
#         elif hasattr(obj, 'user'):
#             owner_field = obj.user
#         elif hasattr(obj, 'patient') and hasattr(obj.patient, 'user_account'): # Example for patient-linked data
#             # This part is hypothetical, assumes Patient model has a 'user_account' field linking to User
#             owner_field = obj.patient.user_account
#
#         return (owner_field and owner_field == request.user) or (request.user and request.user.is_staff)
