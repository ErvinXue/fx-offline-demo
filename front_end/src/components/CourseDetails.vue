<script setup>
import { defineProps, ref } from "vue";
import {
  NCard,
  NSpace,
  NButton,
  NImage,
  NH3,
  NP,
  NTag,
  NIcon,
  NModal,
  useMessage,
} from "naive-ui";
import { PeopleCircleOutline } from "@vicons/ionicons5";
import { createOrder } from "../api/order";
const props = defineProps(["course", "isPurchased"]);
const showPurchase = ref(false);
const message = useMessage();
const purchase = async () => {
  const response = await createOrder(props.course.id);
  showPurchase.value = false;
  message.success(`Success,here is your order: ${response.id}`);
};
</script>
<template>
  <n-card>
    <div class="course-card-body">
      <n-image width="300" :src="props.course.cover_image"></n-image>

      <n-space vertical class="course-info">
        <n-h3>{{ props.course.name }}</n-h3>
        <n-space>
          <n-p>
            Price: <span> ${{ props.course.original_price }}</span>
          </n-p>
          <n-p>
            Lecturer: <span> {{ props.course.teacher.display_name }}</span>
          </n-p>
          <n-p>
            Campus: <span> {{ props.course.campus.name }}</span>
          </n-p>
        </n-space>
        <n-tag type="success" round :bordered="false" class="count-tag">
          Enrolled: {{ props.course.students_count }}
          <template #icon>
            <n-icon :component="PeopleCircleOutline"></n-icon>
          </template>
        </n-tag>
        <n-p class="desc"> {{ props.course.description }}</n-p>
        <n-button
          class="purchase-button"
          type="primary"
          @click="showPurchase = true"
          v-if="isPurchased === false">
          Course purchase
        </n-button>
      </n-space>
    </div>
  </n-card>
  <n-modal
    v-model:show="showPurchase"
    preset="dialog"
    title="Course purchase"
    content="Do you want to buy this course"
    positive-text="Place an order"
    negative-text="Cancel the order"
    @positive-click="purchase"
  />
</template>

<style lang="less" scoped>
.course-card-body {
  display: flex;
}
.course-info {
  padding: 16px;
  padding-left: 32px;
  width: 100%;
  height: 100%;
  span {
    font-size: 16px;
    font-weight: 700;
    margin-left: 12px;
    margin-right: 16px;
  }
  .desc {
    margin-top: 16px;
  }
  .purchase-button {
    position: absolute;
    bottom: 30px;
    right: 30px;
  }
  .count-tag {
    margin-top: 1rem;
  }
}
</style>
