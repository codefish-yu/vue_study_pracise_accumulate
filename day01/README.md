功能:
1. 当无todos时只显示第一栏 v-show="todos.length
2. 添加todo
3. 动态显示todos列表(根据过滤按钮和addtodo动态显示)
4. 显示未完todos数
5. 全选复选框,全选时未完成数显示为0,显示clear completed按钮(clear complete清空已完成todos)
6. 单选按钮,当todo被单选时表示已完成,显示clear completed按钮
7. 删除todo按钮
8. 三个过滤按钮:all,active,completed   
all:显示所有todos
active:只显示未完成todos
complete:只显示已完成todos
