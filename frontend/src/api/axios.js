import axios from 'axios'
const BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'
const instance = axios.create({ baseURL: BASE })

instance.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export default instance
