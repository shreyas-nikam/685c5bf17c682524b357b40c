
# Personalized Upskilling Recommender - AI Risk Score - V3

## Overview

The "Personalized Upskilling Recommender" is a Streamlit application designed to help individuals assess and mitigate their risk of AI-driven job displacement. It provides a personalized assessment based on an individual's current occupation, skills, and learning progress. By leveraging a multi-factor risk model, the application calculates an **AI-Q score**, identifies skill gaps, suggests relevant learning resources, and allows users to track their progress, directly illustrating the concept of **Idiosyncratic Risk Mitigation**.

This application transforms complex actuarial and economic models into an intuitive, interactive tool, making the abstract concept of AI displacement risk tangible and actionable for individuals. It specifically demonstrates how different skill types (general vs. firm-specific) impact an individual's Idiosyncratic Risk score.

## Features

*   **Risk Assessment**: Input your professional details to get a personalized AI-Q score, breaking down your vulnerability into Human Capital, Company Risk, and Upskilling factors.
*   **Upskilling Path**: Discover high-impact general and firm-specific skills relevant to your occupation and get personalized learning resource recommendations. Simulate career transitions to see how they affect your risk.
*   **Progress Tracking**: Monitor changes in your AI-Q score and estimated monthly premium as you acquire new skills or transition to new roles.
*   **Interactive Visualizations**: Understand risk contributions and trends over time with dynamic charts.
*   **Transparent Model**: All mathematical formulae used in the calculation are explained in LaTeX within the application, ensuring clarity and educational value.

## Core Concepts Explained

The application implements a sophisticated multi-factor risk model, including:

*   **Idiosyncratic Risk (Vulnerability)**: Your personal susceptibility to job displacement, influenced by your human capital, company stability, and upskilling efforts.
    $$
    V_{i}(t) = \text{normalized}(FHC \cdot (w_{CR} \cdot FCR + w_{US} \cdot FUS))
    $$
*   **Human Capital Factor ($FHC$)**: Your foundational resilience based on education, experience, role, and institution.
    $$
    FHC = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
    $$
*   **Company Risk Factor ($FCR$)**: Quantifies your employer's stability and growth prospects.
    $$
    FCR = w_{1} \cdot S_{senti} + w_{2} \cdot S_{fin} + w_{3} \cdot S_{growth}
    $$
*   **Upskilling Factor ($FUS$)**: Reflects proactive training efforts, with a higher emphasis on portable skills.
    $$
    F_{US} = 1 - (\gamma_{gen} P_{gen}(t) + \gamma_{spec} P_{spec}(t))
    $$
*   **Systematic Risk (Hazard) ($H_{i}$)**: Macro-level automation hazard for your occupation, adjusted by economic climate and AI innovation pace.
    $$
    H_{i} = H_{base}(t) \cdot (w_{econ} M_{econ} + w_{inno} I_{AI})
    $$
*   **Annual Claim Probability ($P_{claim}$)**: The joint probability of a systemic event and individual loss.
    $$
    P_{claim} = P_{systemic} \cdot P_{individual|systemic}
    $$
*   **Expected Loss ($E[Loss]$)**: The potential financial impact of job displacement.
    $$
    E[Loss] = P_{claim} \cdot L_{payout}
    $$
*   **Monthly Premium ($P_{monthly}$)**: The estimated monthly cost for an "AI displacement insurance" based on your risk.
    $$
    P_{monthly} = \max\left(\frac{E[Loss] \cdot \lambda}{12}, P_{min}\right)
    $$

## Installation and Usage

To run this application locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Personalized-Upskilling-Recommender
    ```
    *(Note: Replace `<repository_url>` with the actual URL if this were a real repository.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    The application will open in your default web browser at `http://localhost:8501`.

## Docker Usage

You can also run the application using Docker:

1.  **Build the Docker image:**
    ```bash
    docker build -t ai-risk-recommender .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8501:8501 ai-risk-recommender
    ```

    Access the application in your browser at `http://localhost:8501`.

## Project Structure

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## License

© 2025 QuantUniversity. All Rights Reserved.
The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.
