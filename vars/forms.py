from fotutils.forms import ModelFormWithSlugBase
from vars.models import Var, Device


class VarForm(ModelFormWithSlugBase):

    class Meta(ModelFormWithSlugBase.Meta):
        model = Var


class DeviceForm(ModelFormWithSlugBase):

    class Meta(ModelFormWithSlugBase.Meta):
        model = Device