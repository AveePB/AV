from datetime import datetime
from pathlib import Path
import csv

class CSVManager:
    """
        CSV file manager collects data about AV's drive informations.
    """
    
    def __init__(self, path: str):
        """
            Constructor that creates/reads a file and constructs basic manager.

            Args:
                path (str): source path to the csv file.
        """
        
        self.__source_path = Path(path)
        self.__records = []
        self.__load_data()

    def __load_data(self):
        """
            Loads data from the csv file.
        """
        
        if (self.__source_path.exists()):
            
            with open(self.__source_path, 'r') as f:
                reader = csv.DictReader(f)
                self.__records = list(reader)

            return True
        else:
            return False
        
    def __save_data(self):
        """
            Save currently stored data to the location of the csv file.
        """        
        
        table_headers = ['id', 'created_at', 'maneuver'] + [ str(i) for i in range(360)]

        # Create new file
        with open(self.__source_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=table_headers)
            writer.writeheader()
            writer.writerows(self.__records)
    
    def number_of_records(self):
        """
            Getter function that returns the current length of the self.__records.
        """

        return len(self.__records)

    def create_record(self, maneuver, degrees):
        """
            Creates a new record to the csv file out of the given data.

            Args:
                maneuver (Maneuver): the current maneuver of the AV.
                degrees (list): the list of integers (360 metrices).
        """

        # Safety check
        if (maneuver == None or degrees == None or len(degrees) != 360): return False

        # Create basic row structure
        new_scan = {
            'id': len(self.__records) + 1,
            'created_at': datetime.now().isoformat(),
            'maneuver': maneuver,
        }

        # Add columns (for each degree)
        for i in range(360): new_scan[str(i)] = degrees[i]

        # Update and reload database
        self.__records.append(new_scan)
        self.__save_data()
        
        return True