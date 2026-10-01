struct Node{
    char data;
    struct Node*prev;
};

struct stack{
   struct Node*top;
};

bool is_empty(struct stack stack){
   if(stack.top==NULL){
    return true;
   }
   return false;
}

void push(struct stack *stack,char val){
    
    struct Node*newnode=(struct Node*)malloc(sizeof(struct Node));
    newnode->prev=NULL;
    newnode->data=val;
    newnode->prev=stack->top;
    stack->top=newnode;
}

char pop(struct stack*stack){
    
    if(is_empty(*stack)){
       printf("stack underflow\n");
        return -1;
    }

    char val=stack->top->data;
    struct Node*temp=stack->top;
    stack->top=stack->top->prev;
    free(temp);
    return val;
}

char peek(struct stack*stack){
    
    if(is_empty(*stack)){
       printf("stack underflow\n");
        return -1;
    }

    return stack->top->data;
    
}
bool is_valid(char a,char b){
    if((a=='['&&b!=']')||(a=='{'&&b!='}')|| (a=='('&&b!=')') ){

        return false;
    }

    return true;
}

bool is_balanced(char str[]){
    int n=strlen(str);

   
    struct stack s;
     s.top=NULL;

    for(int i=0;i<n;i++){
        char a=str[i];

        if(a=='{'||a=='['||a=='('){
            push(&s,a);
    
        }
         if(a=='}'||a==']'||a==')'){
            
            if(is_empty(s)){
                return false;
            }
            if(!is_valid(pop(&s),a)){
               return false;
            }
        }
    }

    return is_empty(s);
    
}

bool isValid(char* s) {
    return is_balanced(s);
}