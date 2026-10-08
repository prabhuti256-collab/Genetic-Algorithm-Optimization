import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Genetic Algorithm Optimizer",
    page_icon="🧬",
    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title("🧬 Genetic Algorithm Optimizer")

st.markdown(
    """
    **Evolutionary optimization using selection, crossover,
    mutation, and natural selection.**
    """
)

st.divider()


# ==================================================
# OBJECTIVE FUNCTIONS
# ==================================================

def current_function(x):
    return x * np.sin(10 * np.pi * x) + 1


def sphere_function(x):
    return x ** 2


def rastrigin_function(x):
    return (
        10
        + x ** 2
        - 10 * np.cos(2 * np.pi * x)
    )


def ackley_function(x):
    return (
        -20
        * np.exp(
            -0.2 * np.sqrt(
                0.5 * x ** 2
            )
        )
        - np.exp(
            0.5 * np.cos(
                2 * np.pi * x
            )
        )
        + np.e
        + 20
    )


# ==================================================
# FUNCTION SETTINGS
# ==================================================

functions = {
    "Non-linear Function": {
        "function": current_function,
        "bounds": (-1, 2)
    },

    "Sphere Function": {
        "function": sphere_function,
        "bounds": (-10, 10)
    },

    "Rastrigin Function": {
        "function": rastrigin_function,
        "bounds": (-5.12, 5.12)
    },

    "Ackley Function": {
        "function": ackley_function,
        "bounds": (-5, 5)
    }
}


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("⚙️ Optimization Settings")

selected_function = st.sidebar.selectbox(
    "Objective Function",
    list(functions.keys())
)

function_info = functions[selected_function]

objective_function = function_info["function"]

default_bounds = function_info["bounds"]


optimization_type = st.sidebar.selectbox(
    "Optimization Goal",
    [
        "Minimize",
        "Maximize"
    ]
)


population_size = st.sidebar.slider(
    "Population Size",
    min_value=10,
    max_value=200,
    value=50,
    step=10
)


generations = st.sidebar.slider(
    "Generations",
    min_value=10,
    max_value=500,
    value=100,
    step=10
)


mutation_rate = st.sidebar.slider(
    "Mutation Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.10,
    step=0.05
)


crossover_rate = st.sidebar.slider(
    "Crossover Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.80,
    step=0.05
)


# ==================================================
# FUNCTION INFORMATION
# ==================================================

st.subheader("📌 Selected Function")

if selected_function == "Non-linear Function":

    st.latex(
        r"f(x) = x\sin(10\pi x) + 1"
    )

elif selected_function == "Sphere Function":

    st.latex(
        r"f(x) = x^2"
    )

elif selected_function == "Rastrigin Function":

    st.latex(
        r"f(x) = 10 + x^2 - 10\cos(2\pi x)"
    )

else:

    st.latex(
        r"\text{Ackley Function}"
    )


st.write(
    f"Search range: `{default_bounds[0]}` to `{default_bounds[1]}`"
)


# ==================================================
# RUN BUTTON
# ==================================================

run_algorithm = st.button(
    "🚀 Run Genetic Algorithm",
    use_container_width=True
)


if run_algorithm:

    maximize = (
        optimization_type == "Maximize"
    )

    # ----------------------------------------------
    # CREATE GENETIC ALGORITHM
    # ----------------------------------------------

    ga = GeneticAlgorithm(
        fitness_function=objective_function,
        bounds=default_bounds,
        population_size=population_size,
        generations=generations,
        mutation_rate=mutation_rate,
        crossover_rate=crossover_rate,
        maximize=maximize
    )

    # ----------------------------------------------
    # RUN OPTIMIZATION
    # ----------------------------------------------

    with st.spinner(
        "Running genetic algorithm..."
    ):

        result = ga.run()

    # Support either 2 or 3 returned values
    if len(result) == 3:

        (
            best_solution,
            best_fitness,
            history
        ) = result

    else:

        (
            best_solution,
            best_fitness
        ) = result

        history = ga.fitness_history

    # ----------------------------------------------
    # SAVE RESULTS
    # ----------------------------------------------

    st.session_state.ga = ga
    st.session_state.best_solution = best_solution
    st.session_state.best_fitness = best_fitness
    st.session_state.history = history
    st.session_state.selected_function = selected_function
    st.session_state.default_bounds = default_bounds

    st.success(
        "Optimization completed successfully!"
    )


# ==================================================
# DISPLAY RESULTS IF AVAILABLE
# ==================================================

if "ga" in st.session_state:

    ga = st.session_state.ga

    best_solution = st.session_state.best_solution

    best_fitness = st.session_state.best_fitness

    history = st.session_state.history

    current_bounds = st.session_state.default_bounds

    # ==================================================
    # RESULTS
    # ==================================================

    st.subheader(
        "📊 Optimization Results"
    )

    initial_fitness = history[0]

    improvement = abs(
        best_fitness - initial_fitness
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Best Solution",
            f"{best_solution:.6f}"
        )

    with col2:

        st.metric(
            "Best Fitness",
            f"{best_fitness:.6f}"
        )

    with col3:

        st.metric(
            "Generations",
            generations
        )

    with col4:

        st.metric(
            "Fitness Improvement",
            f"{improvement:.6f}"
        )


    # ==================================================
    # CONVERGENCE GRAPH
    # ==================================================

    st.subheader(
        "📈 Fitness Convergence"
    )

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        range(
            1,
            len(history) + 1
        ),
        history,
        linewidth=2
    )

    ax.set_xlabel(
        "Generation"
    )

    ax.set_ylabel(
        "Best Fitness"
    )

    ax.set_title(
        "Fitness Improvement Over Generations"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    st.pyplot(fig)


    # ==================================================
    # POPULATION EVOLUTION
    # ==================================================

    st.subheader(
        "🧬 Population Evolution"
    )

    st.write(
        """
        The scatter plot below shows how the population of
        candidate solutions changes during the optimization process.
        """
    )

    # Check population history

    if not hasattr(ga, "population_history"):

        st.warning(
            "Population history is not available in the GeneticAlgorithm class."
        )

    elif len(ga.population_history) == 0:

        st.warning(
            "No population history was recorded."
        )

    else:

        available_generations = len(
            ga.population_history
        )

        selected_generation = st.slider(
            "Select Generation",
            min_value=1,
            max_value=available_generations,
            value=available_generations,
            step=1
        )

        population = ga.population_history[
            selected_generation - 1
        ]

        population_fitness = np.array([
            objective_function(x)
            for x in population
        ])

        # ------------------------------------------
        # FUNCTION VALUES
        # ------------------------------------------

        x_values = np.linspace(
            current_bounds[0],
            current_bounds[1],
            1000
        )

        y_values = np.array([
            objective_function(x)
            for x in x_values
        ])

        # ------------------------------------------
        # POPULATION GRAPH
        # ------------------------------------------

        fig_population, ax_population = plt.subplots(
            figsize=(10, 5)
        )

        ax_population.plot(
            x_values,
            y_values,
            linewidth=2,
            label="Objective Function"
        )

        ax_population.scatter(
            population,
            population_fitness,
            s=50,
            alpha=0.7,
            label="Population"
        )

        ax_population.scatter(
            best_solution,
            best_fitness,
            s=150,
            marker="*",
            label="Best Solution"
        )

        ax_population.set_xlabel(
            "x"
        )

        ax_population.set_ylabel(
            "f(x)"
        )

        ax_population.set_title(
            f"Population at Generation {selected_generation}"
        )

        ax_population.legend()

        ax_population.grid(
            True,
            alpha=0.3
        )

        st.pyplot(
            fig_population
        )


    # ==================================================
    # FUNCTION GRAPH
    # ==================================================

    st.subheader(
        "📉 Objective Function"
    )

    x_values = np.linspace(
        current_bounds[0],
        current_bounds[1],
        1000
    )

    y_values = np.array([
        objective_function(x)
        for x in x_values
    ])

    fig2, ax2 = plt.subplots(
        figsize=(10, 5)
    )

    ax2.plot(
        x_values,
        y_values,
        linewidth=2,
        label="Objective Function"
    )

    ax2.scatter(
        best_solution,
        best_fitness,
        s=120,
        label="Best Solution"
    )

    ax2.set_xlabel(
        "x"
    )

    ax2.set_ylabel(
        "f(x)"
    )

    ax2.set_title(
        "Optimal Solution"
    )

    ax2.legend()

    ax2.grid(
        True,
        alpha=0.3
    )

    st.pyplot(fig2)


    # ==================================================
    # ALGORITHM STEPS
    # ==================================================

    st.subheader(
        "🧠 Genetic Algorithm Process"
    )

    process_col1, process_col2 = st.columns(2)

    with process_col1:

        st.markdown(
            """
            **1️⃣ Population Initialization**

            Random candidate solutions are generated.

            **2️⃣ Fitness Evaluation**

            Each candidate is evaluated using the objective function.

            **3️⃣ Selection**

            Better candidates are selected as parents.
            """
        )

    with process_col2:

        st.markdown(
            """
            **4️⃣ Crossover**

            Parent solutions are combined to create children.

            **5️⃣ Mutation**

            Small random changes maintain population diversity.

            **6️⃣ Evolution**

            The process repeats until the final generation.
            """
        )


    # ==================================================
    # PARAMETERS USED
    # ==================================================

    st.subheader(
        "⚙️ Parameters Used"
    )

    parameter_data = {

        "Parameter": [
            "Objective Function",
            "Optimization Goal",
            "Population Size",
            "Generations",
            "Mutation Rate",
            "Crossover Rate",
            "Search Range"
        ],

        "Value": [
            selected_function,
            optimization_type,
            population_size,
            generations,
            mutation_rate,
            crossover_rate,
            str(default_bounds)
        ]
    }

    st.table(
        parameter_data
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Genetic Algorithm Optimization | "
    "Python • NumPy • Matplotlib • Streamlit"
)
