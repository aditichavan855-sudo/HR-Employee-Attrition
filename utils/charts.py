import plotly.express as px

# =====================================================
# COMMON LAYOUT
# =====================================================

def apply_layout(fig, title):

    fig.update_layout(
        title=title,
        template="plotly",
        height=420,
        title_x=0.02,
        title_font_size=20,
        margin=dict(l=20, r=20, t=55, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend_title=None,
        font=dict(size=14)
    )

    return fig


# =====================================================
# ATTRITION PIE
# =====================================================

def attrition_pie(df):

    attrition = (
        df["Attrition"]
        .value_counts()
        .reset_index()
    )

    attrition.columns = ["Attrition", "Count"]

    fig = px.pie(
        attrition,
        names="Attrition",
        values="Count",
        hole=0.55,
        color="Attrition",
        color_discrete_map={
            "Yes": "#EF4444",
            "No": "#22C55E"
        }
    )

    fig.update_traces(
        textinfo="percent+label",
        marker=dict(
            line=dict(
                color="white",
                width=2
            )
        )
    )

    return apply_layout(fig, "🥧 Attrition Distribution")


# =====================================================
# DEPARTMENT ATTRITION
# =====================================================

def department_chart(df):

    dept = (
        df.groupby("Department")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Attrition Rate")
    )

    fig = px.bar(
        dept,
        x="Department",
        y="Attrition Rate",
        color="Department",
        text_auto=".1f"
    )

    fig.update_traces(
        marker_line_color="#374151",
        marker_line_width=1.5,
        textposition="outside"
    )

    return apply_layout(fig, "🏢 Department Attrition")


# =====================================================
# GENDER ATTRITION
# =====================================================

def gender_chart(df):

    gender = (
        df.groupby("Gender")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Attrition Rate")
    )

    fig = px.bar(
        gender,
        x="Gender",
        y="Attrition Rate",
        color="Gender",
        text_auto=".1f"
    )

    fig.update_traces(
        marker_line_color="#374151",
        marker_line_width=1.5,
        textposition="outside"
    )

    return apply_layout(fig, "👩 Gender Analysis")


# =====================================================
# OVERTIME ANALYSIS
# =====================================================

def overtime_chart(df):

    overtime = (
        df.groupby("OverTime")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Attrition Rate")
    )

    fig = px.bar(
        overtime,
        x="OverTime",
        y="Attrition Rate",
        color="OverTime",
        text_auto=".1f"
    )

    fig.update_traces(
        marker_line_color="#374151",
        marker_line_width=1.5,
        textposition="outside"
    )

    return apply_layout(fig, "⏰ Overtime Analysis")


# =====================================================
# AGE DISTRIBUTION
# =====================================================

def age_distribution(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=20,
        color_discrete_sequence=["#3B82F6"]
    )

    fig.update_traces(
        marker_line_color="#374151",
        marker_line_width=1.3
    )

    return apply_layout(fig, "🎂 Age Distribution")


# =====================================================
# MONTHLY INCOME DISTRIBUTION
# =====================================================

def income_distribution(df):

    fig = px.histogram(
        df,
        x="MonthlyIncome",
        nbins=20,
        color_discrete_sequence=["#10B981"]
    )

    fig.update_traces(
        marker_line_color="#374151",
        marker_line_width=1.3
    )

    return apply_layout(fig, "💰 Monthly Income Distribution")