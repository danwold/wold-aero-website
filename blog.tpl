%rebase layout

%for f in blog:
       {{f.date}}
       <br>
       {{f.text}}
<hr>
%end


