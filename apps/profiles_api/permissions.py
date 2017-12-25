from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit only their own profile """

    # it returns true or false. True if user is trying to change his own profile
    def has_object_permission(self, request, view, obj):
        """ Check the user who is trying to change the profile, only allow if user.id == id of user making the change"""

        print('esto es request method: ', request.method)

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id