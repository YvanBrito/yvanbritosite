import axios from 'axios'

var url = 'http://yvanbrito.com';

const api = axios.create({
    baseURL: url,
    headers: {'Content-Type': 'application/json'}
})

export default api
