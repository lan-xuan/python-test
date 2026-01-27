import api from './axios'
export const login = (username, password) => api.post('/api/auth/token', new URLSearchParams({username, password}))
