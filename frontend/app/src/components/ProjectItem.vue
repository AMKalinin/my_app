<template>
    <fieldset class="project">
        <legend>Name: {{project.name}}</legend>
        
        <div class="imgBlock">
            <!-- {% if ( 9 > project.task.all) %}
                {% for i in range(project.task.all)%}
                <img class="img_icon" src="{{url_for('general.task_icon', project_name=project.name, task_index=i)}}">
                {% endfor %}
            {% else %}
                {% for i in range(9)%}
                <img class="img_icon" src="{{url_for('general.task_icon', project_name=project.name, task_index=i)}}">
                {% endfor %}
            {% endif %} -->
        </div>

        <div>
            <p>
                Tasks: {{ project.task.done }} / {{ project.task.all }} <br> <br>
                Modified: {{ project.lastUpdate }}
            </p>
        </div>
        
        <div class="buttonOpenProject">
            <button @click="$router.push('/tasks')">Open</button>
        </div>
    </fieldset>
</template>


<script>
export default{
    props:{
        project:{
            type: Object,
            required: true
        }
    }
}

</script>

<style>
.project{
    height: 180px;
    border: 1px solid #E4E4E4;
    margin:30px;
    min-width: 890px;
    position: sticky;
    
    padding-left: 12px;
    padding-right: 12px;
    padding-top: 6px;
    padding-bottom: 6px;
}

.imgIcon{
    margin-right: 25px;
    width: 60px;
    height: 60px;
}

.buttonOpenProject{
    position: absolute;
    top: 20px; 
    right: 20px;
}

.buttonOpenProject button{
    width: 90px;
    height: 25px;
    background: #F6F8FA;
    border: 1px solid #D5D8DA;
    border-radius: 6px;
    font-size: 90%;
}

</style>