from prism_business_api.filters import BusinessFilters
from prism_business_api.scope import BUSINESS_PREFIXES, apply_business_scope, business_codes


def test_business_codes_measured_shape():
    codes = business_codes()
    assert len(codes) == 138 and list(codes) == sorted(codes)      # 5 + 93 + 40 on 2026-09-13
    assert 0 in codes and 55 in codes                               # Company News, Venture Capital
    assert BUSINESS_PREFIXES == ("/News/Business News", "/Business & Industrial", "/Finance")


def test_default_scope_is_injected_as_classes():
    f, scope = apply_business_scope(BusinessFilters(q="tariff"))
    assert scope["applied"] == "default" and scope["class_count"] == 138
    assert f.classes and len(f.classes.split(",")) == 138 and f.q == "tariff"


def test_caller_classes_win():
    f, scope = apply_business_scope(BusinessFilters(classes="0"))
    assert scope["applied"] == "caller" and f.classes == "0"
    f, scope = apply_business_scope(BusinessFilters(class_prefix="/Sports"))
    assert scope["applied"] == "caller" and f.classes is None and f.class_prefix == "/Sports"
