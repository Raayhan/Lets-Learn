<template>
    <div class="bg-gray-100 border rounded group flex flex-col h-full">
        <router-link :to="course.get_absolute_url" class="flex flex-col h-full">
            <figure class="mb-4">
                <img :src="course.get_image"
                    class="w-full h-48 rounded-t group-hover:opacity-70 transition-opacity duration-300"
                    alt="Course Thumbnail">
            </figure>
            <div class="flex flex-col justify-between flex-grow">
                <div class="mx-2 leading-tighter">
                    <h3 class="text-violet-800 text-sm font-medium mb-1">{{ course.title }}</h3>
                </div>
                <div class="mx-2 mb-4 leading-tighter">
                    <div class="flex">
                        <h3 class="text-green-800 flex text-xs font-medium mr-2 items-center">
                            <BxSolidCategoryAlt /> &nbsp;{{ course.category }}
                        </h3>
                        <h3 class="text-gray-500 text-xs flex">
                            <CaUserAvatarFilledAlt /> &nbsp;
                            {{ course.author.first_name }} {{ course.author.last_name }}
                        </h3>
                    </div>
                </div>
            </div>
        </router-link>
    </div>


</template>
<script>
import { BxSolidCategoryAlt } from '@kalimahapps/vue-icons';
import { CaUserAvatarFilledAlt } from '@kalimahapps/vue-icons';
export default {
    name: 'CourseBox',
    props: {
        course: Object
    },
    components: {
        BxSolidCategoryAlt,
        CaUserAvatarFilledAlt
    }

}
</script>