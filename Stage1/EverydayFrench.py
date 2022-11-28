import Model
import GUI.View as View
import Controller
import pandas as pd
import os


def main():
    
    file = os.getcwd() + '\Stage1\data.csv'
    data = pd.read_csv(file, low_memory = False)

    model = Model.Model(data)
    controller = Controller.Controller(model)

    controller.execute()
    
    


if __name__ == "__main__":
    main()