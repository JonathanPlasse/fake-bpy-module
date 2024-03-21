from docutils.parsers.rst import roles
from docutils import nodes


class PythonAPIRef(nodes.Inline, nodes.TextElement):
    def astext(self) -> str:
        name = super().astext()

        return f"`{name}`"

    def to_string(self) -> str:
        return super().astext()


class ClassRef(PythonAPIRef):
    tagname = "class-ref"


class MethodRef(PythonAPIRef):
    tagname = "method-ref"


class AttributeRef(PythonAPIRef):
    tagname = "attribute-ref"


class FunctionRef(PythonAPIRef):
    tagname = "function-ref"


class ModuleRef(PythonAPIRef):
    tagname = "module-ref"


class DataRef(PythonAPIRef):
    tagname = "data-ref"


class ConstRef(PythonAPIRef):
    tagname = "const-ref"


class RefRef(PythonAPIRef):
    tagname = "ref-ref"


class ExcRef(PythonAPIRef):
    tagname = "exc-ref"


def register_roles():
    roles.register_local_role("class", roles.GenericRole("class", ClassRef))
    roles.register_local_role("meth", roles.GenericRole("meth", MethodRef))
    roles.register_local_role("attr", roles.GenericRole("attr", AttributeRef))
    roles.register_local_role("func", roles.GenericRole("func", FunctionRef))
    roles.register_local_role("mod", roles.GenericRole("mod", ModuleRef))
    roles.register_local_role("data", roles.GenericRole("data", DataRef))
    roles.register_local_role("const", roles.GenericRole("const", ConstRef))
    roles.register_local_role("ref", roles.GenericRole("ref", RefRef))
    roles.register_local_role("exc", roles.GenericRole("exc", ExcRef))
