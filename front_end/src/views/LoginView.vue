<script setup>
import {
  NA,
  NSpace,
  NForm,
  NFormItem,
  NInput,
  NH1,
  NH5,
  NButton,
  useMessage,
} from "naive-ui";
import { useRouter } from "vue-router";
import { computed, ref } from "vue";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const authStore = useAuthStore();

const message = useMessage();
const formRef = ref(null);
const loginModel = ref({
  username: "admin",
  password: "password",
});

const loading = ref(false);
const disabled = computed(
  () => loginModel.value.username === "" || loginModel.value.password === ""
);
 
const handleLogin = async () => {
  loading.value = true;
  try {
    await authStore.login(loginModel.value.username, loginModel.value.password);
    loading.value = true;
    const redirectUrl =
      router.currentRoute.value.query.redirect?.toString() || "/";
    await router.replace(redirectUrl);}catch (e) {
    message.error(e.response.data.message);
    
  }

};
</script>
<template>
  <div class="login">
    <n-space class="login-card" vertical>
      <n-h1>Welcome to Fangxue Offline</n-h1>
      <n-h5>Please login to continue.</n-h5>
      <n-form ref="formRef" :model="loginModel">
        <n-form-item path="username" label="Username">
          <n-input
            type="text"
            placeholder="Please Input"
            v-model:value="loginModel.username"
          />
        </n-form-item>
        <n-form-item path="password" label="Password">
          <n-input
            type="password"
            placeholder="Please Input"
            v-model:value="loginModel.password"
          />
        </n-form-item>
        <n-space justify="space-between" align="center">
          <n-a href="/forget"> Forget your password? </n-a>
          <n-space>
            <n-button size="large" tag="a" href="/register">
              Register
            </n-button>
            <n-button
              type="primary"
              tag="a"
              size="large"
              :loading="loading"
              :disabled="disabled"
              @click="handleLogin"
            >
              Login
            </n-button>
          </n-space>
        </n-space>
      </n-form>
    </n-space>
  </div>
</template>
<style lang="less" scoped>
.login {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: end;
  align-items: center;
}
.login-card {
  margin-right: 18vw;
}
</style>
