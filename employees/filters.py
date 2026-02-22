import django_filters as djf

from .models import Employee


class EmployeeFilter(djf.FilterSet):
    designation = djf.CharFilter(field_name="designation", lookup_expr="iexact")
    emp_name = djf.CharFilter(field_name="emp_name", lookup_expr="icontains")

    id_min = djf.CharFilter(method="filter_by_id_range", label="From EMP ID")
    id_max = djf.CharFilter(method="filter_by_id_range", label="To EMP ID")

    class Meta:
        model = Employee
        fields = ["designation", "emp_name", "id_min", "id_max"]

    def filter_by_id_range(self, queryset, name, value):
        if name == "id_min":
            return queryset.filter(emp_id__gte=value)
        elif name == "id_max":
            return queryset.filter(emp_id__lte=value)
        return queryset
