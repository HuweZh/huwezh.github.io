<template>
  <v-md-preview :text="markdown"></v-md-preview>
</template>

<script>
export default {
  data() {
    return {
      markdown: '### 标题',
    };
  },
};
</script>