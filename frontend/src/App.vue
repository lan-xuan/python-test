<template>
  <el-container>
    <el-header>
      <el-menu
        :default-active="activeMenu"
        mode="horizontal"
        router
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="/dashboard">
          <el-icon><House /></el-icon>
          <span>Dashboard</span>
        </el-menu-item>
        <el-menu-item index="/users">
          <el-icon><User /></el-icon>
          <span>Users</span>
        </el-menu-item>
        <el-menu-item index="/menus">
          <el-icon><Menu /></el-icon>
          <span>Menus</span>
        </el-menu-item>
        <el-menu-item index="/logs">
          <el-icon><Document /></el-icon>
          <span>Logs</span>
        </el-menu-item>
        <el-menu-item index="/db">
          <el-icon><DataLine /></el-icon>
          <span>Database</span>
        </el-menu-item>
        <div class="flex-grow"></div>
        <el-menu-item index="/login" v-if="!isLoggedIn">
          <el-icon><Lock /></el-icon>
          <span>Login</span>
        </el-menu-item>
        <el-menu-item @click="handleLogout" v-else>
          <el-icon><SwitchButton /></el-icon>
          <span>Logout</span>
        </el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { House, User, Menu, Document, DataLine, Lock, SwitchButton } from '@element-plus/icons-vue'

const route = useRoute()
const router = useRouter()

const activeMenu = computed(() => route.path)

const isLoggedIn = computed(() => !!localStorage.getItem('token'))

const handleLogout = () => {
  localStorage.removeItem('token')
  ElMessage.success('Logged out')
  router.push('/login')
}
</script>

<style scoped>
.el-header {
  padding: 0;
  background-color: #545c64;
}

.flex-grow {
  flex-grow: 1;
}

.el-main {
  padding: 20px;
}
</style>

