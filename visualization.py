import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, df):
        """Initialize the DataVisualizer class with the dataframe."""
        self.df = df

    def plot_churn_pie_chart(self):
        """Plot a pie chart showing the distribution of Churn."""
        ax = self.df['Churn'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Pie Chart of Churn', figsize=(6, 6))
        ax.legend(['No', 'Yes'])
        plt.show()

    def plot_histograms(self):
        """Plot histograms for MonthlyCharges and TotalCharges."""
        plt.figure(figsize=(12, 5))

        # Histogram for MonthlyCharges
        plt.subplot(1, 2, 1)
        plt.hist(self.df['MonthlyCharges'], bins=6, edgecolor='k')
        plt.title('Histogram of Monthly Charges')
        plt.xlabel('Monthly Charges')
        plt.ylabel('Frequency')

        # Histogram for TotalCharges
        plt.subplot(1, 2, 2)
        plt.hist(self.df['TotalCharges'], bins=7, edgecolor='k')
        plt.title('Histogram of Total Charges')
        plt.xlabel('Total Charges')
        plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()

    def plot_contract_churn(self):
        """Plot the distribution of Contract type with respect to Churn."""
        sns.countplot(data=self.df, x='Contract', hue='Churn')
        plt.title('Distribution of Contract Type by Churn')
        plt.show()

    def plot_boxplot_churn_vs_tenure(self):
        """Plot a boxplot showing Churn vs Tenure."""
        sns.boxplot(x='Churn', y='tenure', data=self.df)
        plt.title('Churn vs. Tenure')
        plt.show()

    def plot_boxplot_churn_vs_monthly_charges(self):
        """Plot a boxplot showing Churn vs Monthly Charges."""
        sns.boxplot(x='Churn', y='MonthlyCharges', data=self.df)
        plt.title('Churn vs. Monthly Charges')
        plt.show()

    def plot_scatter_tenure_vs_monthly_charges(self):
        """Plot a scatterplot of Tenure vs Monthly Charges, colored by Churn."""
        sns.scatterplot(x='tenure', y='MonthlyCharges', hue='Churn', data=self.df)
        plt.title('Tenure vs. Monthly Charges (Colored by Churn)')
        plt.show()

    def plot_pairplot(self):
        """Plot a pairplot for tenure, MonthlyCharges, TotalCharges, and Churn."""
        sns.pairplot(self.df[['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']], hue='Churn')
        plt.suptitle('Pair Plot of Tenure, Monthly Charges, and Total Charges by Churn', y=1.02)
        plt.show()

    def plot_correlation_heatmap(self):
        """Plot a heatmap showing the correlation between numerical features."""
        numerical_features = self.df[['tenure', 'MonthlyCharges', 'TotalCharges']]
        corr = numerical_features.corr()
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Heatmap: Correlation Matrix of Tenure, Monthly Charges, and Total Charges')
        plt.show()

# Usage
if __name__ == "__main__":
    from loading import DataLoader  # Assuming DataLoader is in loading.py
    from preprocessing import DataPreprocessor  # Assuming DataPreprocessor is in preprocessing.py

    # Load and preprocess the data
    loader = DataLoader(r'C:\Users\aruni\Desktop\customer churn project\Telco-Customer-Churn.csv')
    data = loader.load_data()

    preprocessor = DataPreprocessor(data)
    preprocessor.convert_total_charges()
    preprocessor.drop_unwanted_columns()

    # Visualize the data
    visualizer = DataVisualizer(data)

    # Call the different visualizations
    visualizer.plot_churn_pie_chart()
    visualizer.plot_histograms()
    visualizer.plot_contract_churn()
    visualizer.plot_boxplot_churn_vs_tenure()
    visualizer.plot_boxplot_churn_vs_monthly_charges()
    visualizer.plot_scatter_tenure_vs_monthly_charges()
    visualizer.plot_pairplot()
    visualizer.plot_correlation_heatmap()
