import data.RawData as RawData
import util.file as file
if __name__ == '__main__':
    rawdata=RawData()
    rawdata.dispose(file.getRootPath()+'data\sample.json')
    rawdata.save(file.getRootPath()+'data\dataBase\\rawData.csv')