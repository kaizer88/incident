from django import template
from lib.helper import DictDiffer
from django.forms.models import model_to_dict

register = template.Library()

@register.assignment_tag
def get_vehicle_history(vehicle_history, field_changed = None):

    response_list = []
    
    prev = vehicle_history.get_previous_by_history_date()
    vehicle_dict = model_to_dict(vehicle_history)
    prev_vehicle_dict = model_to_dict(prev)

    changes = DictDiffer(vehicle_dict, prev_vehicle_dict).changed()
    
    
    for change in changes:

        if "history" not in change:
            if field_changed:
                if field_changed == change:
                    response = {}
                    response[change.replace('_',' ')] = {"from_val": getattr(prev, change).__str__(),
                                                 "to_val": getattr(vehicle_history, change).__str__()}
                    response_list.append(response)
            else:
                response = {}
                response[change.replace('_',' ')] = {"from_val": getattr(prev, change).__str__(),
                                                 "to_val": getattr(vehicle_history, change).__str__()}
                response_list.append(response)

    return response_list