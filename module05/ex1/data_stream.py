from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod

class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0
        
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    @abstractmethod
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria"""
        return data_batch
        

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "stream_processed_count": self.processed_count,
        }

class SensorStream(DataStream):
    """Data stream implementation for enviromental sensor data"""

    def __init__(self, stream_id: str):
        """Initialize the sensor stream and set avg temperature to zero."""
        super().__init__(stream_id, "Enviromental Data")
        self.avg_temp: float = 0.0

    def process_batch(self, data_batch: List[str]) -> str:
        """Parse temperature readings and calculate the average."""
        temps = []
        for item in data_batch:
            pair = item.split(":")
            if pair[0] == "temp":
                try:
                    temps.append(float(pair[1]))
                except ValueError:
                    print(f"Warning: invalid tempature '{pair[1]}'")
        if temps:
            self.avg_temp = sum(temps) / len(temps)
        else:
            self.avg_temp = 0.0
        
        self.processed_count += len(data_batch)
        return (
            f"Sensor analysis: {self.processed_count} readings processed,"
            f"avg temp: {self.avg_temp:.1f}°C"
        )
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific statistics."""
        base = super().get_stats()
        base["avg_temp"] = self.avg_temp
        return base
    
    def filter_data(
            self, data_batch: List[str], criteria: Optional[str] = None
    ) -> List[str]:
        """Filter sensor data .Criteria='critical': temp < 15 or temp > 30."""
        critical, normal = [], []
        for item in data_batch:
            pair = item.split(":")
            if len(pair) != 2 or pair[0] != "temp":
                continue
            try:
                temp = float(pair[1])
            except ValueError:
                continue
            if temp < 15 or temp > 30:
                critical.append(item)
            else:
                normal.append(item)
        if criteria == "critical":
            return critical 
        return normal



class TransactionStream(DataStream):


class StreamProcessor(DataStream):


class StreamProcessor():


class 