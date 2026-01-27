<template>
  <el-container style="height:100vh; align-items:center; justify-content:center">
    <el-form :model="form" @submit.prevent="onSubmit" style="width:360px">
      <h2>Login</h2>
      <el-form-item>
        <el-input v-model="form.username" placeholder="Username" />
      </el-form-item>
      <el-form-item>
        <el-input v-model="form.password" placeholder="Password" show-password />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Login</el-button>
      </el-form-item>
    </el-form>
  </el-container>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { login } from '../api/auth'

const router = useRouter()
const form = reactive({ username: '', password: '' })

async function onSubmit() {
  try {
    const res = await login(form.username, form.password)
    localStorage.setItem('token', res.data.access_token)
    ElMessage.success('Logged in')
    router.push('/dashboard')
  } catch (e) {
    ElMessage.error('Login failed')
  }
}
</script>
