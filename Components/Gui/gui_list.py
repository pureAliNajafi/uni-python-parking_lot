import pandas as pd
from Components.Gui import gui
def gui_list(message:str,data:list[dict[str, any]],filtered_columns:list[str] =[],index: bool=False) -> None:
    
    gui.print(message) 

    df = pd.DataFrame(data)
    df_filtered_columns = df.drop(columns=filtered_columns)
    if index:
        print(df_filtered_columns)
    else:
        print(df_filtered_columns.to_string(index=False))
        