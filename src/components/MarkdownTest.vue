<template>
  <v-md-preview :text="markdown"></v-md-preview>
</template>

<script>
// import demo from "../assets/demo.md"
import axios from "axios"
export default {
  data() {
    const markdown = "";
    const url = "./md/demo.md";
    axios.get(url).then((response) => {
      console.log(response);
      this.markdown = response.data;
    });
    return {
      markdown: markdown,
    };
  },
};
</script>