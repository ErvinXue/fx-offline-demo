<script setup>
import { ref, defineProps, computed } from "vue";
import {
  NCard,
  NThing,
  NTag,
  NSpace,
  NAvatar,
  NIcon,
  NDescriptions,
  NDescriptionsItem,
  NDivider,
  NA,
  NModal,
  NUpload,
  NUploadDragger,
  useMessage,
} from "naive-ui";
import { uploadAttachment } from "../api/course";
import {VideocamSharp,
    DocumentAttachOutline,
    CloudUploadOutline,
    LinkOutline} from "@vicons/ionicons5"
const scheduled_time = computed(
  () => new Date(props.lecture.scheduled_time + "Z")
);
const showUpload = ref(false);
const handleAddNewAttachment = () => {
  showUpload.value = true;
};
const props = defineProps(["lecture", "courseId", "isAdmin"])
const message = useMessage();
const uploadRequest = async ({ file, onFinish, onError, onProgress }) => {
  try {
    await uploadAttachment(
      props.courseId,
      props.lecture.id,
      file.file,
      file.name,
      "attachment",
      ({ percent }) => {
        onProgress({ percent: Math.ceil(percent) });
      }
    );
    onFinish();
    message.success("File Uploaded. Page will be reload within 1.5 seconds");
    setTimeout(() => window.location.reload(), 1500);
  } catch (e) {
    onError();
  }
};
</script> 

<template>
    <n-card>
        <n-thing>
            <template #avatar>
                <n-icon :component="VideocamSharp"/>
            </template>
            <template #header> {{ props.lecture.title }} </template>
            <template #header-extra>{{ scheduled_time.toLocaleDateString() }}
            </template>
            
      <n-descriptions label-placement="left" :column="1">
        <n-descriptions-item label="Time">
          {{ scheduled_time.toLocaleString() }}
        </n-descriptions-item>
        <n-descriptions-item label="Streaming">
          <n-a :href="props.lecture.streaming_url">Start Zoom meeting</n-a>
        </n-descriptions-item>
        <n-descriptions-item label="Recording">
          <n-a :href="props.lecture.recording_url">Start Zoom meeting</n-a>
        </n-descriptions-item>
    </n-descriptions>
    <template #footer>
        <n-divider class="attachment-divider">Attachments </n-divider>
        <n-space>
            <n-tag
            v-for="attachment in props.lecture.attachments"
            :key="attachment.name"
            round
            :bordered="false"
            size="small"
            type="success"
          >
            <template #icon>
              <n-icon :component="DocumentAttachOutline"></n-icon>
            </template>
            <n-a :href="attachment.Signed_url"> {{ attachment.name }} </n-a>
          </n-tag>
          <n-tag
            v-if="isAdmin"
            round
            :bordered="false"
            size="small"
            type="success"
          >
            <template #icon>
              <n-icon :component="CloudUploadOutline"></n-icon>
            </template>
            <n-a @click="handleAddNewAttachment"> Upload +</n-a>
          </n-tag>
        </n-space>



    </template>
        </n-thing>
    </n-card>
    <n-modal v-model:show="showUpload">
    <n-card
      style="width: 300px"
      title="Upload new attachment"
      :bordered="false"
      size="huge"
    >
      <n-upload directory-dnd="false" :custom-request="uploadRequest">
        <n-upload-dragger>
          <div style="margin-bottom: 12px">
            <n-icon size="48" :depth="3" :component="LinkOutline"></n-icon>
          </div>
          Click or drag to add
        </n-upload-dragger>
      </n-upload>
    </n-card>
  </n-modal>
</template>



<style scoped>
.lecture-id {
  font-size: 12px;
  color: gray;
}
.attachment-divider {
  font-size: 12px;
  color: gray;
}
</style>