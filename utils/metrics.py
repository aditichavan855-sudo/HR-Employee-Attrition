def calculate_metrics(df):
    """Calculate dashboard KPIs."""

    # Convert Yes/No to 1/0
    attrition_numeric = df["Attrition"].map({
        "Yes": 1,
        "No": 0
    })

    return {
        "total_employees": len(df),

        "attrition_rate": round(
            attrition_numeric.mean() * 100,
            1
        ),

        "average_age": round(
            df["Age"].mean(),
            1
        ),

        "average_income": round(
            df["MonthlyIncome"].mean(),
            0
        )
    }
