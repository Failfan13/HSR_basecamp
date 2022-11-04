import raspData from '../data_collection/raspData.json' assert {type: 'json'};

export default function dataArrs(data = raspData){
    const temp = []
    const time = []
    const humid = []
    const press = []
    data.forEach(a => {
        time.push(a['timestamp']),
        temp.push(a['temperature'])
        humid.push(a['humidity'])
        press.push(a['pressure'])
    })
    return {'time': time, 'temp': temp, 'humid': humid, 'press': press}
}
