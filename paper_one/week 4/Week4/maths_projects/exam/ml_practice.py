"""
ML FOUNDATIONS PRACTICE PROGRAM
================================
Covers: Math -> Statistics -> Probability -> Distributions -> Correlation -> Statistical Thinking

How to use:
    python3 ml_practice.py

You'll get a menu. Pick a topic, answer questions typed into the terminal.
Numeric answers are checked with a small tolerance (so 70.0 and 70 both count).
Type 'skip' on any question to see the worked answer and move on.
Type 'quit' at the menu to exit.

This is a PRACTICE tool, not a teaching tool - it assumes you already know
the concepts (mean, variance, probability, correlation, etc.) and just want
to test your own logic against real numbers.
"""

import random
import statistics
import numpy as np


# ---------------------------------------------------------------------------
# Small helper for checking numeric answers with tolerance
# ---------------------------------------------------------------------------
def ask_numeric(question, correct_answer, explanation, tolerance=0.05):
    print("\n" + question)
    user_input = input("Your answer: ").strip().lower()

    if user_input == "skip":
        print(f"Answer: {correct_answer}\nWhy: {explanation}")
        return

    try:
        user_value = float(user_input)
    except ValueError:
        print("That wasn't a number - here's the answer instead.")
        print(f"Answer: {correct_answer}\nWhy: {explanation}")
        return

    if abs(user_value - correct_answer) <= tolerance * max(1, abs(correct_answer)):
        print("Correct!")
    else:
        print(f"Not quite. Correct answer: {correct_answer}")
    print(f"Why: {explanation}")


def ask_text(question, acceptable_answers, explanation):
    """acceptable_answers: list of lowercase strings that count as correct"""
    print("\n" + question)
    user_input = input("Your answer: ").strip().lower()

    if user_input == "skip":
        print(f"Answer: {acceptable_answers[0]}\nWhy: {explanation}")
        return

    if any(ans in user_input for ans in acceptable_answers):
        print("Correct!")
    else:
        print(f"Not quite. Expected something like: {acceptable_answers[0]}")
    print(f"Why: {explanation}")


def section_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# TOPIC 1: MATH FOUNDATIONS
# ---------------------------------------------------------------------------
def topic_math():
    section_header("TOPIC 1: MATH FOUNDATIONS")

    # Randomized linear equation, so it's different each run
    m = random.randint(2, 6)
    b = random.randint(-5, 10)
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [m * x + b for x in x_vals]

    print(f"\nData points: x = {x_vals}, y = {y_vals}")
    ask_numeric(
        "What is the slope (m) of this line? (look at how much y changes per step of x)",
        m,
        "m = (change in y) / (change in x), and that change is constant for a straight line."
    )
    ask_numeric(
        "What is the y-intercept (b)? (plug in one known point into y = m*x + b and solve)",
        b,
        f"Using x={x_vals[0]}, y={y_vals[0]}: {y_vals[0]} = {m}*{x_vals[0]} + b, solve for b."
    )

    test_x = random.randint(6, 10)
    predicted_y = m * test_x + b
    ask_numeric(
        f"Using y = {m}x + {b}, what would y be when x = {test_x}?",
        predicted_y,
        f"Substitute x={test_x} into the equation directly."
    )


# ---------------------------------------------------------------------------
# TOPIC 2: STATISTICS
# ---------------------------------------------------------------------------
def topic_stats():
    section_header("TOPIC 2: STATISTICS FUNDAMENTALS")

    data = random.sample(range(50, 100), 6)
    print(f"\nDataset: {data}")

    ask_numeric(
        "What is the MEAN of this dataset? (sum divided by count)",
        statistics.mean(data),
        f"sum({data}) = {sum(data)}, divided by {len(data)} values."
    )

    sorted_data = sorted(data)
    ask_numeric(
        f"What is the MEDIAN? (hint: sort first -> {sorted_data})",
        statistics.median(data),
        "With an even count, median = average of the two middle values."
    )

    ask_numeric(
        "What is the sample VARIANCE? (use n-1 in the denominator, since this is a sample)",
        statistics.variance(data),
        "variance = sum of squared differences from the mean, divided by (n-1) for a sample."
    )

    ask_numeric(
        "What is the sample STANDARD DEVIATION? (square root of variance)",
        statistics.stdev(data),
        "std dev = sqrt(variance) - brings the units back to normal (not squared)."
    )

    ask_text(
        "This dataset - is it a POPULATION or a SAMPLE? (assume it's a handful of scores from a much bigger class)",
        ["sample"],
        "Unless your data covers EVERY member of the group you care about, it's a sample - "
        "which is why we divided by n-1 above, not n."
    )


# ---------------------------------------------------------------------------
# TOPIC 3: PROBABILITY
# ---------------------------------------------------------------------------
def topic_probability():
    section_header("TOPIC 3: PROBABILITY FUNDAMENTALS")

    red, blue, green = random.randint(5, 15), random.randint(5, 15), random.randint(3, 10)
    total = red + blue + green
    print(f"\nBag contents: {red} red, {blue} blue, {green} green marbles")

    ask_numeric(
        "Total marbles in the bag?",
        total,
        "Just add every color's count together."
    )

    ask_numeric(
        "P(red) as a decimal? (favorable / total)",
        red / total,
        f"{red} red marbles out of {total} total."
    )

    ask_text(
        "You pick a marble, put it BACK, then pick again. Is the second pick independent or dependent?",
        ["independent"],
        "Replacing the marble resets the bag to its original state - nothing changed for the next pick."
    )

    new_total = total - 1
    new_red = red - 1
    ask_numeric(
        f"You pick RED and do NOT replace it. What is P(red) on the SECOND pick now? "
        f"(remaining red = {new_red}, remaining total = {new_total})",
        new_red / new_total,
        "One red marble and one total marble were removed from the bag - recalculate the fraction."
    )

    # Conditional probability / Bayes style question
    print("\nA disease affects 2% of a population. A test correctly detects it 90% of the time "
          "(true positive rate), and gives a false positive 8% of the time.")
    p_disease = 0.02
    p_pos_given_disease = 0.90
    p_pos_given_no_disease = 0.08
    p_positive = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * (1 - p_disease))
    p_disease_given_positive = (p_pos_given_disease * p_disease) / p_positive

    ask_numeric(
        "What is P(testing positive) overall, combining both sick and healthy people? "
        "(Hint: P(pos|disease)*P(disease) + P(pos|no disease)*P(no disease))",
        p_positive,
        f"({p_pos_given_disease}*{p_disease}) + ({p_pos_given_no_disease}*{1-p_disease})"
    )

    ask_numeric(
        "Using Bayes' theorem, what is P(disease | positive test)? "
        "(Hint: [P(pos|disease) * P(disease)] / P(positive))",
        p_disease_given_positive,
        "This is usually much lower than people expect - rare disease + imperfect test = many false alarms."
    )


# ---------------------------------------------------------------------------
# TOPIC 4: DATA DISTRIBUTIONS
# ---------------------------------------------------------------------------
def topic_distributions():
    section_header("TOPIC 4: DATA DISTRIBUTIONS")

    data = [22, 24, 23, 25, 21, 24, 23, 22, 95]  # one clear outlier
    print(f"\nDataset: {data}")

    mean_val = np.mean(data)
    median_val = np.median(data)

    ask_text(
        "Is mean expected to be HIGHER or LOWER than median here, given that one large value (95)?",
        ["higher"],
        "A single large outlier drags the mean up, since mean is sensitive to extreme values; "
        "median barely moves since it just looks at the middle position."
    )

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    upper_bound = q3 + 1.5 * iqr

    ask_numeric(
        f"Using the IQR method (Q1={q1:.2f}, Q3={q3:.2f}), what is the IQR (Q3 - Q1)?",
        iqr,
        "IQR = Q3 - Q1, the range of the middle 50% of the data."
    )

    ask_numeric(
        "What is the upper outlier boundary? (Q3 + 1.5 * IQR)",
        upper_bound,
        f"{q3:.2f} + 1.5 * {iqr:.2f}"
    )

    ask_text(
        "Which value in the dataset would be flagged as an outlier by this boundary?",
        ["95"],
        f"95 is above the upper boundary of {upper_bound:.2f}, while everything else is well below it."
    )

    ask_text(
        "Is this dataset RIGHT-skewed or LEFT-skewed? (the tail stretches which direction?)",
        ["right"],
        "The outlier (95) pulls a long tail out to the RIGHT (high values) - remember, skew is named "
        "after the tail direction, not where most of the data sits."
    )


# ---------------------------------------------------------------------------
# TOPIC 5: CORRELATION
# ---------------------------------------------------------------------------
def topic_correlation():
    section_header("TOPIC 5: CORRELATION & RELATIONSHIPS")

    hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
    exam_score = [50, 55, 62, 68, 74, 79, 85, 90]
    r = np.corrcoef(hours_studied, exam_score)[0, 1]

    print(f"\nhours_studied = {hours_studied}")
    print(f"exam_score    = {exam_score}")

    ask_text(
        "Just by looking at the two lists - positive, negative, or no relationship?",
        ["positive"],
        "As hours_studied goes up, exam_score also consistently goes up."
    )

    ask_numeric(
        "What is the correlation coefficient r between these two? (use np.corrcoef if you want to check)",
        r,
        "np.corrcoef(hours_studied, exam_score)[0, 1] gives this directly.",
        tolerance=0.02
    )

    ask_text(
        "TRUE or FALSE: this correlation PROVES that studying more CAUSES higher scores.",
        ["false"],
        "Correlation only shows they move together - it doesn't rule out confounding variables "
        "or prove direct causation, even when a causal story seems very plausible."
    )

    # Confounding variable question
    print("\nScenario: ice cream sales and shark attacks are strongly positively correlated.")
    ask_text(
        "What is the most likely explanation - direct causation, or a confounding variable? If confounding, name it.",
        ["confound", "hot weather", "temperature", "summer"],
        "Hot weather independently increases both ice cream sales and ocean swimming (hence shark attacks) - "
        "neither one causes the other directly."
    )


# ---------------------------------------------------------------------------
# TOPIC 6: STATISTICAL THINKING FOR ML
# ---------------------------------------------------------------------------
def topic_statistical_thinking():
    section_header("TOPIC 6: STATISTICAL THINKING FOR ML")

    ask_text(
        "You survey customers by only asking people who volunteer to fill out a form. "
        "What type of bias is this?",
        ["sampling", "self-selection", "selection"],
        "Only certain kinds of people (often those with strong opinions) bother to volunteer - "
        "this is a classic sampling bias, meaning your data doesn't represent the true population."
    )

    ask_text(
        "A model fits its training data almost perfectly, but performs badly on new data it hasn't seen. "
        "Is this a sign of HIGH BIAS or HIGH VARIANCE?",
        ["variance"],
        "This is classic overfitting - the model is too complex, so it learned the specific noise "
        "in its training data rather than the true underlying pattern (high variance)."
    )

    ask_text(
        "A model performs poorly even on its OWN training data. Is this HIGH BIAS or HIGH VARIANCE?",
        ["bias"],
        "This is underfitting - the model is too simple to capture the real pattern at all (high bias)."
    )

    ask_numeric(
        "You have data on ALL 30 employees at a small company (not a subset). "
        "Should you divide variance by n or n-1? Answer with the number of employees you'd divide by (30 or 29).",
        30,
        "Since this data IS the entire population (all 30 employees, no one left out), "
        "use population variance, dividing by N (30), not n-1."
    )

    ask_text(
        "An A/B test shows p-value = 0.03 for a new website design increasing sales. "
        "Does this PROVE the new design causes more sales, or just suggest it's unlikely due to chance?",
        ["suggest", "unlikely", "evidence", "not proof", "likely"],
        "A low p-value is evidence the difference probably isn't random chance - it's not absolute proof, "
        "and practical significance (is $2 extra sales actually meaningful?) still needs separate judgment."
    )


# ---------------------------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------------------------
TOPICS = {
    "1": ("Math Foundations", topic_math),
    "2": ("Statistics Fundamentals", topic_stats),
    "3": ("Probability Fundamentals", topic_probability),
    "4": ("Data Distributions", topic_distributions),
    "5": ("Correlation & Relationships", topic_correlation),
    "6": ("Statistical Thinking for ML", topic_statistical_thinking),
}


def main():
    print("ML FOUNDATIONS PRACTICE PROGRAM")
    print("Type a number to practice that topic, 'all' to run everything in order, or 'quit' to exit.\n")

    while True:
        for key, (name, _) in TOPICS.items():
            print(f"  {key}. {name}")
        choice = input("\nChoice: ").strip().lower()

        if choice == "quit":
            print("Good work today - see you next session.")
            break
        elif choice == "all":
            for _, func in TOPICS.values():
                func()
        elif choice in TOPICS:
            TOPICS[choice][1]()
        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()
