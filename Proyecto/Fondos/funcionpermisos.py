#!/usr/bin/env python
# -*- coding: utf-8 -*

from django.contrib.auth.decorators import user_passes_test

###############################
#  Función que mira los grupos y
# si el nombre de un usuario esta
###############################


def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')
