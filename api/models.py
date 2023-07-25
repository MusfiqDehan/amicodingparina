from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.exceptions import BadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from khoj.models import Input


class InputResource(ModelResource):
    class Meta:
        queryset = Input.objects.all()
        resource_name = 'items'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True
        allowed_methods = ['get']

    def obj_get_list(self, bundle):
        # Get the parameters
        start_datetime = bundle.request.GET.get('start_datetime', None)
        end_datetime = bundle.request.GET.get('end_datetime', None)
        user_id = bundle.request.GET.get('user_id', None)

        # If all the parameters are provided, filter the results
        if start_datetime and end_datetime and user_id:
            try:
                user = User.objects.get(id=user_id)
            except ObjectDoesNotExist:
                raise BadRequest("No user found with id: {0}".format(user_id))

            results = Input.objects.filter(
                user=user, timestamp__gte=start_datetime, timestamp__lte=end_datetime)

        # Else, return all results
        else:
            results = Input.objects.all()

        return results
