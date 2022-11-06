export function createChart(canvas, labels, dataObject) {
    const dataset = []
    dataObject.forEach(key => {dataset.push({
        label: key['title'],
        data: key['points'],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        pointStyle: 'crossRot',
        pointRadius: 5,
        borderWidth: 2,
        tension: 0.1,
        fill: false,
    })})
    new Chart(canvas, {
        type: 'line',
        data: {
            labels: labels,
            datasets: dataset
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                },
            }
        }
    });
}

export function createChartData(servData, title){
    const data = []
    const servTime = []
    for (let i in servData) {
        if (i == 'time') {
            servData[i].sort();
            servData[i].forEach(i => {
                const date = new Date(i*1000);
                servTime.push(date.getHours()+'.'+date.getMinutes())
            })
        } 
        if (i == title) {
            let title = '';
            let servDataConvert = []
            if (i == 'temp') {
                title = 'Temperature over time';
            } else if (i == 'humid'){
                title = 'Humidity over time'
            } else {
                title = 'Pressure / 25 over time'
                servData[i].forEach(i => {
                    servDataConvert.push(i/25)
                })
                servData[i] = servDataConvert
            }
            data.push({'title': title, 'points' : servData[i]})
            break
        }
    }
    return [servTime, data]
}