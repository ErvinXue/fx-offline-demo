<script setup>
import { NCard, NSpace, NH2, NP, NAvatar, NTag, NIcon } from "naive-ui";
import { defineProps,computed } from "vue";
const props = defineProps(["userInfo"]);
import { Bonfire } from "@vicons/ionicons5";
const userType = computed(() => props.userInfo.user_type.split(".")[1]);
</script>

<template #default>
<n-card
    :segmented="{
      content: true,
      footer: 'soft',
    }">
    <n-space justify="space-between" align="center">
    <n-space vertical>
    <n-h2> Welcome {{ props.userInfo.display_name }}</n-h2>
    <n-p> User ID: {{ props.userInfo.id }}</n-p>
    <n-p> Current campus: {{ props.userInfo.campus }}</n-p>
</n-space>
<n-avatar :size="88" round>
    <img src="~@/assets/house.png" alt="" />
</n-avatar>
</n-space> <template #footer>
    <n-space> <n-tag type="info" round :bordered="false"> {{ userType }}
        <template #icon>
            <n-icon :component="Bonfire"></n-icon>
          </template></n-tag>
          <n-tag 
          size="small"
          type="warning"
          v-for="permission in props.userInfo.permissions"
          round
          :key="permission"
          :bordered="false"
        >
          {{ permission }}
        </n-tag>
    </n-space>
</template>
</n-card>
 <!-- {{ props.userInfo }} -->
</template>