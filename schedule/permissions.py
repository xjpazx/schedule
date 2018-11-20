from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
METHODS = ('PUT', 'PATCH')


class AssignmentPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_assignment')):
            return True
        elif request.method in METHODS and (request.user.is_superuser
                                            or request.user.has_perm('schedule.change_assignment')):
            return True
        elif (request.method == 'DELETE') and (request.user.is_superuser
                                               or request.user.has_perm('schedule.delete_assignment')):
            return True
    #METHODS2 = ('GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST')


class ActivityPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_activity')):
            return True
        elif request.method == 'POST' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_activity')):
            return True
        elif request.method in METHODS and (request.user.is_superuser
                                            or request.user.has_perm('schedule.change_activity')):
            return True
        elif (request.method == 'DELETE') and (request.user.is_superuser
                                               or request.user.has_perm('schedule.delete_activity')):
            return True


class EmployeePermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_user')):
            return True
        elif request.method == 'POST' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_user')):
            return True
        elif request.method in METHODS and (request.user.is_superuser
                                            or request.user.has_perm('schedule.change_user')):
            return True
        elif (request.method == 'DELETE') and (request.user.is_superuser
                                               or request.user.has_perm('schedule.delete_user')):
            return True


class TruckPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_truck')):
            return True
        elif request.method == 'POST' and (request.user.is_superuser
                                           or request.user.has_perm('schedule.add_truck')):
            return True
        elif request.method in METHODS and (request.user.is_superuser
                                            or request.user.has_perm('schedule.change_truck')):
            return True
        elif (request.method == 'DELETE') and (request.user.is_superuser
                                               or request.user.has_perm('schedule.delete_truck')):
            return True