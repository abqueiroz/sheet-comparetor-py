# Worker benefits form field to SSA payload mappings
FORM_FIELD_2_SSA_PAYLOAD_CSS_WORKER_BENEFITS_INFO = {
    "grant-equity": {"path": ["compensation", "equity"]},
    "supplemental-plans": {"path": ["electiveBenefits"]},
    "medical-allowance": {
        "path": ["compensation", "allowances"],
        "children": {
            "type-of-allowances": {
                "path": ["type"],
            },
            "allowance_amounts": {"path": ["amount", "value"]},
        },
    },
}

# Worker time off form field to SSA payload mappings
FORM_FIELD_2_SSA_PAYLOAD_CSS_WORKER_TIME_OFF_INFO = {
    "vacation-premium": {"path": ["vacationPremium"]},
    "total-vacation-accrual-days": {"path": ["timeOffDays", "value"]}
}