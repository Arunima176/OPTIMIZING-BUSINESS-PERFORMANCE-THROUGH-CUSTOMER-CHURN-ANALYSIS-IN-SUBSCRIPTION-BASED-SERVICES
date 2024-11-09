from loading import DataLoader
from preprocessing import DataPreprocessor
from visualization import DataVisualizer

def main():
    try:
        loader = DataLoader(r'C:\Users\aruni\Desktop\customer churn project\Telco-Customer-Churn.csv')
        data = loader.load_data()

        print("First few rows of the dataset:\n", loader.display_head())
        print("Dataset shape:", loader.display_shape())
        print("Summary statistics:\n", loader.display_summary())
  
        preprocessor = DataPreprocessor(data)
        preprocessor.check_info()
        preprocessor.convert_total_charges()
        preprocessor.drop_unwanted_columns()
        preprocessor.display_shape()
        preprocessor.final_check()

        visualizer = DataVisualizer(data)
        visualizer.plot_churn_pie_chart()
        visualizer.plot_histograms()
        visualizer.plot_contract_churn()
        visualizer.plot_boxplot_churn_vs_tenure()
        visualizer.plot_boxplot_churn_vs_monthly_charges()
        visualizer.plot_scatter_tenure_vs_monthly_charges()
        visualizer.plot_pairplot()
        visualizer.plot_correlation_heatmap()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

