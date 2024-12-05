[
    {
        "if": {
            "issue": "inventory shortage",
            "cause": "unexpected demand",
            "response_time": "slow"
        },
        "then": {
            "diagnosis": "Insufficient buffer stock for high-demand scenarios.",
            "recommendation": "Increase safety stock and improve demand forecasting."
        }
    },
    {
        "if": {
            "issue": "transport delay",
            "cause": "carrier unavailability",
            "response_time": "slow"
        },
        "then": {
            "diagnosis": "Carrier scheduling not optimized.",
            "recommendation": "Identify alternative carriers and build redundancy."
        }
    },
    {
        "if": {
            "issue": "quality issue",
            "cause": "supplier negligence",
            "response_time": "fast"
        },
        "then": {
            "diagnosis": "Supplier quality assurance failure.",
            "recommendation": "Enforce stricter supplier audits and quality checks."
        }
    },
    {
        "if": {
            "issue": "inventory surplus",
            "cause": "over-ordering",
            "response_time": "moderate"
        },
        "then": {
            "diagnosis": "Order quantities not aligned with actual demand.",
            "recommendation": "Enhance demand planning and align with JIT principles."
        }
    },
    {
        "if": {
            "issue": "cost increase",
            "cause": "transport cost hike",
            "response_time": "moderate"
        },
        "then": {
            "diagnosis": "High dependency on single-mode transport.",
            "recommendation": "Diversify transport modes and negotiate contracts."
        }
    }
]
