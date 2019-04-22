a = #p.1#
b = #p.2#
disp('test matlab project!!!');
fid1=fopen(['results\re_' num2str(a) '_' num2str(b) '.txt'],'w');
fprintf(fid1,' %f %f \n',a,b);
exit;