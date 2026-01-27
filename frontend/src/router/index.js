import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import Users from '../views/Users.vue'
import Menus from '../views/Menus.vue'
import Logs from '../views/Logs.vue'
import DB from '../views/DB.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/users', component: Users },
  { path: '/menus', component: Menus },
  { path: '/logs', component: Logs },
  { path: '/db', component: DB }
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
