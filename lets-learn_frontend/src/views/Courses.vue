<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        Courses
    </div>
    <div v-if="$store.state.setIsLoading" class="flex justify-center mt-4">
        <Loading />
    </div>
</template>
<script>

</script>